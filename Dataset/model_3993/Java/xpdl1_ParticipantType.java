





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ParticipantType  {

    private String name;
    private String id;
    private String description;





    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ExternalReferenceType xpdl1_externalreferencetype;




    private xpdl1_ParticipantTypeType xpdl1_participanttypetype;


    public xpdl1_ParticipantType(
        String name,        String id,        String description    ) {
        this.name = name;
        this.id = id;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ExternalReferenceType getXpdl1_externalreferencetype() {
        return xpdl1_externalreferencetype;
    }

    public void setXpdl1_externalreferencetype(xpdl1_ExternalReferenceType xpdl1_externalreferencetype) {
        this.xpdl1_externalreferencetype = xpdl1_externalreferencetype;
    }
    public xpdl1_ParticipantTypeType getXpdl1_participanttypetype() {
        return xpdl1_participanttypetype;
    }

    public void setXpdl1_participanttypetype(xpdl1_ParticipantTypeType xpdl1_participanttypetype) {
        this.xpdl1_participanttypetype = xpdl1_participanttypetype;
    }

}