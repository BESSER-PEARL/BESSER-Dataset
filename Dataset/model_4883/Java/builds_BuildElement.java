




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class builds_BuildElement  {

    private LocalDate refreshDate;
    private String operations;
    private String elementStatus;
    private String url;
    private String name;





    private List<builds_StringToStringMap> builds_stringtostringmaps;


    public builds_BuildElement(
        LocalDate refreshDate,        String operations,        String elementStatus,        String url,        String name    ) {
        this.refreshDate = refreshDate;
        this.operations = operations;
        this.elementStatus = elementStatus;
        this.url = url;
        this.name = name;
        this.builds_stringtostringmaps = new ArrayList<>();
    }

    public builds_BuildElement(
        LocalDate refreshDate,        String operations,        String elementStatus,        String url,        String name        ArrayList<builds_StringToStringMap> builds_stringtostringmaps    ) {
        this.refreshDate = refreshDate;
        this.operations = operations;
        this.elementStatus = elementStatus;
        this.url = url;
        this.name = name;
        this.builds_stringtostringmaps = builds_stringtostringmaps;
    }

    public LocalDate getRefreshdate() {
        return refreshDate;
    }

    public void setRefreshdate(LocalDate refreshDate) {
        this.refreshDate = refreshDate;
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
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<builds_StringToStringMap> getBuilds_stringtostringmaps() {
        return builds_stringtostringmaps;
    }

    public void addBuilds_stringtostringmap(Builds_stringtostringmap builds_stringtostringmap) {
        this.builds_stringtostringmaps.add(builds_stringtostringmap);
    }

}