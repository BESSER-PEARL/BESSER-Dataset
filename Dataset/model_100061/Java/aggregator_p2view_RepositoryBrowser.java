





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_RepositoryBrowser  {

    private boolean loading;





    private List<MetadataRepositoryStructuredView> metadatarepositorystructuredviews;


    public aggregator_p2view_RepositoryBrowser(
        boolean loading    ) {
        this.loading = loading;
        this.metadatarepositorystructuredviews = new ArrayList<>();
    }

    public aggregator_p2view_RepositoryBrowser(
        boolean loading        ArrayList<MetadataRepositoryStructuredView> metadatarepositorystructuredviews    ) {
        this.loading = loading;
        this.metadatarepositorystructuredviews = metadatarepositorystructuredviews;
    }

    public boolean getLoading() {
        return loading;
    }

    public void setLoading(boolean loading) {
        this.loading = loading;
    }

    public List<MetadataRepositoryStructuredView> getMetadatarepositorystructuredviews() {
        return metadatarepositorystructuredviews;
    }

    public void addMetadatarepositorystructuredview(Metadatarepositorystructuredview metadatarepositorystructuredview) {
        this.metadatarepositorystructuredviews.add(metadatarepositorystructuredview);
    }

}