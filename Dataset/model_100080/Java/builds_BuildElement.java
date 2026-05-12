




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class builds_BuildElement  {

    private String name;
    private String url;
    private String operations;
    private String elementStatus;
    private LocalDate refreshDate;





    private List<builds_StringToStringMap> builds_stringtostringmaps;


    public builds_BuildElement(
        String name,        String url,        String operations,        String elementStatus,        LocalDate refreshDate    ) {
        this.name = name;
        this.url = url;
        this.operations = operations;
        this.elementStatus = elementStatus;
        this.refreshDate = refreshDate;
        this.builds_stringtostringmaps = new ArrayList<>();
    }

    public builds_BuildElement(
        String name,        String url,        String operations,        String elementStatus,        LocalDate refreshDate        ArrayList<builds_StringToStringMap> builds_stringtostringmaps    ) {
        this.name = name;
        this.url = url;
        this.operations = operations;
        this.elementStatus = elementStatus;
        this.refreshDate = refreshDate;
        this.builds_stringtostringmaps = builds_stringtostringmaps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getOperations() {
        return operations;
    }

    public void setOperations(String operations) {
        this.operations = operations;
    }
    public String getElementstatus() {
        return elementStatus;
    }

    public void setElementstatus(String elementStatus) {
        this.elementStatus = elementStatus;
    }
    public LocalDate getRefreshdate() {
        return refreshDate;
    }

    public void setRefreshdate(LocalDate refreshDate) {
        this.refreshDate = refreshDate;
    }

    public List<builds_StringToStringMap> getBuilds_stringtostringmaps() {
        return builds_stringtostringmaps;
    }

    public void addBuilds_stringtostringmap(Builds_stringtostringmap builds_stringtostringmap) {
        this.builds_stringtostringmaps.add(builds_stringtostringmap);
    }

}