





import java.util.List;
import java.util.ArrayList;

public class cjsidl_varFormatField  {

    private String countComment;
    private String units;
    private String comment;
    private String name;
    private String optional;





    private cjsidl_typeDef cjsidl_typedef;




    private cjsidl_recordDef cjsidl_recorddef;


    public cjsidl_varFormatField(
        String countComment,        String units,        String comment,        String name,        String optional    ) {
        this.countComment = countComment;
        this.units = units;
        this.comment = comment;
        this.name = name;
        this.optional = optional;
    }


    public String getCountcomment() {
        return countComment;
    }

    public void setCountcomment(String countComment) {
        this.countComment = countComment;
    }
    public String getUnits() {
        return units;
    }

    public void setUnits(String units) {
        this.units = units;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public cjsidl_recordDef getCjsidl_recorddef() {
        return cjsidl_recorddef;
    }

    public void setCjsidl_recorddef(cjsidl_recordDef cjsidl_recorddef) {
        this.cjsidl_recorddef = cjsidl_recorddef;
    }

}