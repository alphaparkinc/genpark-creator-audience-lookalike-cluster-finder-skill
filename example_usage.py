from client import CreatorAudienceLookalikeClusterFinderClient

def main():
    client = CreatorAudienceLookalikeClusterFinderClient()
    res = client.find_lookalike_creators('@sarah_skincare', 40.0, 'MID_TIER')
    print('Creator Lookalike Cluster Finder: ' + res['cluster_analysis_id'])
    print('Seed: ' + res['seed_creator'] + ' | Cluster Cohesion: ' + str(res['cluster_cohesion_score']))
    print('Matched Creators: ' + str(len(res['matched_lookalike_creators'])) + ' candidates')
    print('Dossier URL: ' + res['audience_lookalike_dossier_url'])

if __name__ == '__main__':
    main()
