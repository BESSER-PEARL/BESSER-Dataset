




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_ProcessComponent extends ProcessPackage {

    private String version;
    private String author;
    private LocalDate changeDate;
    private String copyright;
    private String changeDescription;





    private spem_ProcessComponentUse spem_processcomponentuse;




    private List<spem_WorkProductPort> spem_workproductports;




    private spem_Activity spem_activity;


    public spem_ProcessComponent(
        String version,        String author,        LocalDate changeDate,        String copyright,        String changeDescription    ) {
        super(
        );
        this.version = version;
        this.author = author;
        this.changeDate = changeDate;
        this.copyright = copyright;
        this.changeDescription = changeDescription;
        this.spem_workproductports = new ArrayList<>();
    }

    public spem_ProcessComponent(
        String version,        String author,        LocalDate changeDate,        String copyright,        String changeDescription        ArrayList<spem_WorkProductPort> spem_workproductports    ) {
        this.version = version;
        this.author = author;
        this.changeDate = changeDate;
        this.copyright = copyright;
        this.changeDescription = changeDescription;
        this.spem_workproductports = spem_workproductports;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public LocalDate getChangedate() {
        return changeDate;
    }

    public void setChangedate(LocalDate changeDate) {
        this.changeDate = changeDate;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }

    public spem_ProcessComponentUse getSpem_processcomponentuse() {
        return spem_processcomponentuse;
    }

    public void setSpem_processcomponentuse(spem_ProcessComponentUse spem_processcomponentuse) {
        this.spem_processcomponentuse = spem_processcomponentuse;
    }
    public List<spem_WorkProductPort> getSpem_workproductports() {
        return spem_workproductports;
    }

    public void addSpem_workproductport(Spem_workproductport spem_workproductport) {
        this.spem_workproductports.add(spem_workproductport);
    }
    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }

}