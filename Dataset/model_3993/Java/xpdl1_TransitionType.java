





import java.util.List;
import java.util.ArrayList;

public class xpdl1_TransitionType  {

    private String name;
    private String description;
    private String to;
    private String id;
    private String from_;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_ConditionType xpdl1_conditiontype;




    private xpdl1_TransitionsType xpdl1_transitionstype;


    public xpdl1_TransitionType(
        String name,        String description,        String to,        String id,        String from_    ) {
        this.name = name;
        this.description = description;
        this.to = to;
        this.id = id;
        this.from_ = from_;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_ConditionType getXpdl1_conditiontype() {
        return xpdl1_conditiontype;
    }

    public void setXpdl1_conditiontype(xpdl1_ConditionType xpdl1_conditiontype) {
        this.xpdl1_conditiontype = xpdl1_conditiontype;
    }
    public xpdl1_TransitionsType getXpdl1_transitionstype() {
        return xpdl1_transitionstype;
    }

    public void setXpdl1_transitionstype(xpdl1_TransitionsType xpdl1_transitionstype) {
        this.xpdl1_transitionstype = xpdl1_transitionstype;
    }

}