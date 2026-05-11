





import java.util.List;
import java.util.ArrayList;

public class extended_Form extends FormTypes {

    private String post;
    private String get;
    private String put;
    private String delete;



    public extended_Form(
        String post,        String get,        String put,        String delete    ) {
        super(
        );
        this.post = post;
        this.get = get;
        this.put = put;
        this.delete = delete;
    }


    public String getPost() {
        return post;
    }

    public void setPost(String post) {
        this.post = post;
    }
    public String getGet() {
        return get;
    }

    public void setGet(String get) {
        this.get = get;
    }
    public String getPut() {
        return put;
    }

    public void setPut(String put) {
        this.put = put;
    }
    public String getDelete() {
        return delete;
    }

    public void setDelete(String delete) {
        this.delete = delete;
    }


}