




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class builds_BuildElement  {

    private String operations;
    private String name;
    private String url;
    private LocalDate refreshDate;
    private String elementStatus;





    private List<builds_StringToStringMap> builds_stringtostringmaps;


    public builds_BuildElement(
        String operations,        String name,        String url,        LocalDate refreshDate,        String elementStatus    ) {
        this.operations = operations;
        this.name = name;
        this.url = url;
        this.refreshDate = refreshDate;
        this.elementStatus = elementStatus;
        this.builds_stringtostringmaps = new ArrayList<>();
    }

    public builds_BuildElement(
        String operations,        String name,        String url,        LocalDate refreshDate,        String elementStatus        ArrayList<builds_StringToStringMap> builds_stringtostringmaps    ) {
        this.operations = operations;
        this.name = name;
        this.url = url;
        this.refreshDate = refreshDate;
        this.elementStatus = elementStatus;
        this.builds_stringtostringmaps = builds_stringtostringmaps;
    }

    public String getOperations() {
        return operations;
    }

    public void setOperations(String operations) {
        this.operations = operations;
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
    public LocalDate getRefreshdate() {
        return refreshDate;
    }

    public void setRefreshdate(LocalDate refreshDate) {
        this.refreshDate = refreshDate;
    }
    public String getElementstatus() {
        return elementStatus;
    }

    public void setElementstatus(String elementStatus) {
        this.elementStatus = elementStatus;
    }

    public List<builds_StringToStringMap> getBuilds_stringtostringmaps() {
        return builds_stringtostringmaps;
    }

    public void addBuilds_stringtostringmap(Builds_stringtostringmap builds_stringtostringmap) {
        this.builds_stringtostringmaps.add(builds_stringtostringmap);
    }

}