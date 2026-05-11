





import java.util.List;
import java.util.ArrayList;

public class aml_Memo  {

    private String body;
    private String subject;
    private String type;
    private String id;





    private aml_AmlDocument aml_amldocument;




    private aml_Annotation aml_annotation;


    public aml_Memo(
        String body,        String subject,        String type,        String id    ) {
        this.body = body;
        this.subject = subject;
        this.type = type;
        this.id = id;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public aml_AmlDocument getAml_amldocument() {
        return aml_amldocument;
    }

    public void setAml_amldocument(aml_AmlDocument aml_amldocument) {
        this.aml_amldocument = aml_amldocument;
    }
    public aml_Annotation getAml_annotation() {
        return aml_annotation;
    }

    public void setAml_annotation(aml_Annotation aml_annotation) {
        this.aml_annotation = aml_annotation;
    }

}