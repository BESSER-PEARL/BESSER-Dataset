





import java.util.List;
import java.util.ArrayList;

public class website_CollectionUnit extends SelectableUnit {

    private String emptyMessage;
    private int defaultPaginationSize;
    private boolean useDisabledPageLinks;
    private int nextNpages;
    private int previousNpages;
    private String lastPageLabel;
    private String nextPageLabel;
    private String previousPageLabel;
    private String firstPageLabel;
    private boolean useFirstLastPageLinks;





    private List<website_EntityOrView> website_entityorviews;




    private website_Filter website_filter;




    private website_Selection website_selection;




    private List<website_Filter> website_filters;




    private website_Feature website_feature;


    public website_CollectionUnit(
        String emptyMessage,        int defaultPaginationSize,        boolean useDisabledPageLinks,        int nextNpages,        int previousNpages,        String lastPageLabel,        String nextPageLabel,        String previousPageLabel,        String firstPageLabel,        boolean useFirstLastPageLinks    ) {
        super(
        );
        this.emptyMessage = emptyMessage;
        this.defaultPaginationSize = defaultPaginationSize;
        this.useDisabledPageLinks = useDisabledPageLinks;
        this.nextNpages = nextNpages;
        this.previousNpages = previousNpages;
        this.lastPageLabel = lastPageLabel;
        this.nextPageLabel = nextPageLabel;
        this.previousPageLabel = previousPageLabel;
        this.firstPageLabel = firstPageLabel;
        this.useFirstLastPageLinks = useFirstLastPageLinks;
        this.website_entityorviews = new ArrayList<>();
        this.website_filters = new ArrayList<>();
    }

    public website_CollectionUnit(
        String emptyMessage,        int defaultPaginationSize,        boolean useDisabledPageLinks,        int nextNpages,        int previousNpages,        String lastPageLabel,        String nextPageLabel,        String previousPageLabel,        String firstPageLabel,        boolean useFirstLastPageLinks        ArrayList<website_EntityOrView> website_entityorviews,        ArrayList<website_Filter> website_filters    ) {
        this.emptyMessage = emptyMessage;
        this.defaultPaginationSize = defaultPaginationSize;
        this.useDisabledPageLinks = useDisabledPageLinks;
        this.nextNpages = nextNpages;
        this.previousNpages = previousNpages;
        this.lastPageLabel = lastPageLabel;
        this.nextPageLabel = nextPageLabel;
        this.previousPageLabel = previousPageLabel;
        this.firstPageLabel = firstPageLabel;
        this.useFirstLastPageLinks = useFirstLastPageLinks;
        this.website_entityorviews = website_entityorviews;
        this.website_filters = website_filters;
    }

    public String getEmptymessage() {
        return emptyMessage;
    }

    public void setEmptymessage(String emptyMessage) {
        this.emptyMessage = emptyMessage;
    }
    public int getDefaultpaginationsize() {
        return defaultPaginationSize;
    }

    public void setDefaultpaginationsize(int defaultPaginationSize) {
        this.defaultPaginationSize = defaultPaginationSize;
    }
    public boolean getUsedisabledpagelinks() {
        return useDisabledPageLinks;
    }

    public void setUsedisabledpagelinks(boolean useDisabledPageLinks) {
        this.useDisabledPageLinks = useDisabledPageLinks;
    }
    public int getNextnpages() {
        return nextNpages;
    }

    public void setNextnpages(int nextNpages) {
        this.nextNpages = nextNpages;
    }
    public int getPreviousnpages() {
        return previousNpages;
    }

    public void setPreviousnpages(int previousNpages) {
        this.previousNpages = previousNpages;
    }
    public String getLastpagelabel() {
        return lastPageLabel;
    }

    public void setLastpagelabel(String lastPageLabel) {
        this.lastPageLabel = lastPageLabel;
    }
    public String getNextpagelabel() {
        return nextPageLabel;
    }

    public void setNextpagelabel(String nextPageLabel) {
        this.nextPageLabel = nextPageLabel;
    }
    public String getPreviouspagelabel() {
        return previousPageLabel;
    }

    public void setPreviouspagelabel(String previousPageLabel) {
        this.previousPageLabel = previousPageLabel;
    }
    public String getFirstpagelabel() {
        return firstPageLabel;
    }

    public void setFirstpagelabel(String firstPageLabel) {
        this.firstPageLabel = firstPageLabel;
    }
    public boolean getUsefirstlastpagelinks() {
        return useFirstLastPageLinks;
    }

    public void setUsefirstlastpagelinks(boolean useFirstLastPageLinks) {
        this.useFirstLastPageLinks = useFirstLastPageLinks;
    }

    public List<website_EntityOrView> getWebsite_entityorviews() {
        return website_entityorviews;
    }

    public void addWebsite_entityorview(Website_entityorview website_entityorview) {
        this.website_entityorviews.add(website_entityorview);
    }
    public website_Filter getWebsite_filter() {
        return website_filter;
    }

    public void setWebsite_filter(website_Filter website_filter) {
        this.website_filter = website_filter;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }
    public List<website_Filter> getWebsite_filters() {
        return website_filters;
    }

    public void addWebsite_filter(Website_filter website_filter) {
        this.website_filters.add(website_filter);
    }
    public website_Feature getWebsite_feature() {
        return website_feature;
    }

    public void setWebsite_feature(website_Feature website_feature) {
        this.website_feature = website_feature;
    }

}