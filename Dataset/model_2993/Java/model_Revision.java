





import java.util.List;
import java.util.ArrayList;

public class model_Revision  {

    private String content;
    private String creationDate;





    private model_Content model_content;




    private model_Content model_content;




    private model_User model_user;


    public model_Revision(
        String content,        String creationDate    ) {
        this.content = content;
        this.creationDate = creationDate;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }

    public model_Content getModel_content() {
        return model_content;
    }

    public void setModel_content(model_Content model_content) {
        this.model_content = model_content;
    }
    public model_Content getModel_content() {
        return model_content;
    }

    public void setModel_content(model_Content model_content) {
        this.model_content = model_content;
    }
    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }

}