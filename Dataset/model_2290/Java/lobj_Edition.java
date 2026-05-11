




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_Edition  {

    private LocalDate editionCreationDate;
    private String version;
    private String editedBy;
    private String id;
    private String editionNr;
    private String status;
    private String lastVersionNumber;





    private lobj_AccessControl lobj_accesscontrol;


    public lobj_Edition(
        LocalDate editionCreationDate,        String version,        String editedBy,        String id,        String editionNr,        String status,        String lastVersionNumber    ) {
        this.editionCreationDate = editionCreationDate;
        this.version = version;
        this.editedBy = editedBy;
        this.id = id;
        this.editionNr = editionNr;
        this.status = status;
        this.lastVersionNumber = lastVersionNumber;
    }


    public LocalDate getEditioncreationdate() {
        return editionCreationDate;
    }

    public void setEditioncreationdate(LocalDate editionCreationDate) {
        this.editionCreationDate = editionCreationDate;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getEditedby() {
        return editedBy;
    }

    public void setEditedby(String editedBy) {
        this.editedBy = editedBy;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEditionnr() {
        return editionNr;
    }

    public void setEditionnr(String editionNr) {
        this.editionNr = editionNr;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getLastversionnumber() {
        return lastVersionNumber;
    }

    public void setLastversionnumber(String lastVersionNumber) {
        this.lastVersionNumber = lastVersionNumber;
    }

    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }

}