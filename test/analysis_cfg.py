import FWCore.ParameterSet.Config as cms

process = cms.Process("analysis")

process.load("JetMETCorrections.Configuration.L2L3Corrections_Summer08Redigi_cff")
# set the record's IOV. Must be defined once. Choose ANY correction service. #
process.prefer("L2L3JetCorrectorIC5Calo") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("PhysicsTools.JetMCAlgos.CaloJetsMCFlavour_cfi")

process.load("SimTracker.TrackAssociation.TrackAssociatorByChi2_cfi")

process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("Configuration.StandardSequences.Reconstruction_cff")

#process.load("Configuration.StandardSequences.FakeConditions_cff")

process.load("RecoBTag.PerformanceMeasurements.PerformanceAnalyzer_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep recoJetTags_*_*_*'
    ),
    fileName = cms.untracked.string('test.root')
)

process.Performance.flavourMatchOption = 'genParticle'
process.p = cms.Path(process.caloJetMCFlavour*process.Performance)

readFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource", fileNames = readFiles)
