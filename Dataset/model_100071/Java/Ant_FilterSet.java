





import java.util.List;
import java.util.ArrayList;

public class Ant_FilterSet extends Set {

    private String starttoken;
    private String endtoken;





    private List<Ant_FiltersFile> ant_filtersfiles;




    private List<Ant_Filter> ant_filters;


    public Ant_FilterSet(
        String starttoken,        String endtoken    ) {
        super(
        );
        this.starttoken = starttoken;
        this.endtoken = endtoken;
        this.ant_filtersfiles = new ArrayList<>();
        this.ant_filters = new ArrayList<>();
    }

    public Ant_FilterSet(
        String starttoken,        String endtoken        ArrayList<Ant_FiltersFile> ant_filtersfiles,        ArrayList<Ant_Filter> ant_filters    ) {
        this.starttoken = starttoken;
        this.endtoken = endtoken;
        this.ant_filtersfiles = ant_filtersfiles;
        this.ant_filters = ant_filters;
    }

    public String getStarttoken() {
        return starttoken;
    }

    public void setStarttoken(String starttoken) {
        this.starttoken = starttoken;
    }
    public String getEndtoken() {
        return endtoken;
    }

    public void setEndtoken(String endtoken) {
        this.endtoken = endtoken;
    }

    public List<Ant_FiltersFile> getAnt_filtersfiles() {
        return ant_filtersfiles;
    }

    public void addAnt_filtersfile(Ant_filtersfile ant_filtersfile) {
        this.ant_filtersfiles.add(ant_filtersfile);
    }
    public List<Ant_Filter> getAnt_filters() {
        return ant_filters;
    }

    public void addAnt_filter(Ant_filter ant_filter) {
        this.ant_filters.add(ant_filter);
    }

}