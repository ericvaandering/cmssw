import FWCore.ParameterSet.Config as cms

DQMExample_GenericClient = cms.EDAnalyzer("DQMGenericClient",
                                          subDirs = cms.untracked.vstring("Physics/TopTest"),
                                          efficiency = cms.vstring(
                                              "myEfficiencyEta 'Efficiency vs Eta' EleEta_leading_HLT_matched EleEta_leading",
                                              "myEfficiencyPhi 'Efficiency vs Phi' ElePhi_leading_HLT_matched ElePhi_leading"
                                              ),
                                          resolution = cms.vstring("")
    )
