




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class traceability_Traces  {

    private String originalSourceURL;
    private String location;
    private String fullName;
    private LocalDate date;
    private String comments;
    private String uriMap;
    private String username;





    private List<traceability_EObject> traceability_eobjects;




    private traceability_EObject traceability_eobject;




    private traceability_EObject traceability_eobject;


    public traceability_Traces(
        String originalSourceURL,        String location,        String fullName,        LocalDate date,        String comments,        String uriMap,        String username    ) {
        this.originalSourceURL = originalSourceURL;
        this.location = location;
        this.fullName = fullName;
        this.date = date;
        this.comments = comments;
        this.uriMap = uriMap;
        this.username = username;
        this.traceability_eobjects = new ArrayList<>();
    }

    public traceability_Traces(
        String originalSourceURL,        String location,        String fullName,        LocalDate date,        String comments,        String uriMap,        String username        ArrayList<traceability_EObject> traceability_eobjects    ) {
        this.originalSourceURL = originalSourceURL;
        this.location = location;
        this.fullName = fullName;
        this.date = date;
        this.comments = comments;
        this.uriMap = uriMap;
        this.username = username;
        this.traceability_eobjects = traceability_eobjects;
    }

    public String getOriginalsourceurl() {
        return originalSourceURL;
    }

    public void setOriginalsourceurl(String originalSourceURL) {
        this.originalSourceURL = originalSourceURL;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getUrimap() {
        return uriMap;
    }

    public void setUrimap(String uriMap) {
        this.uriMap = uriMap;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public List<traceability_EObject> getTraceability_eobjects() {
        return traceability_eobjects;
    }

    public void addTraceability_eobject(Traceability_eobject traceability_eobject) {
        this.traceability_eobjects.add(traceability_eobject);
    }
    public traceability_EObject getTraceability_eobject() {
        return traceability_eobject;
    }

    public void setTraceability_eobject(traceability_EObject traceability_eobject) {
        this.traceability_eobject = traceability_eobject;
    }
    public traceability_EObject getTraceability_eobject() {
        return traceability_eobject;
    }

    public void setTraceability_eobject(traceability_EObject traceability_eobject) {
        this.traceability_eobject = traceability_eobject;
    }

}