class CreatorAudienceLookalikeClusterFinderClient:
    def find_lookalike_creators(self, benchmark_creator_handle='@mkbhd', min_audience_overlap_pct=35.0, target_tier='MACRO'):
        return {
            'cluster_analysis_id': 'lok_cls_8812',
            'seed_creator': benchmark_creator_handle,
            'matched_lookalike_creators': [
                {'handle': '@dave2d', 'audience_affinity_similarity_pct': 88.4, 'tier': 'MACRO'},
                {'handle': '@matthew_moniz', 'audience_affinity_similarity_pct': 82.1, 'tier': 'MID_TIER'}
            ],
            'cluster_cohesion_score': 0.94,
            'audience_lookalike_dossier_url': 'https://creators.analytics.genpark.ai/lookalikes/8812.json'
        }
