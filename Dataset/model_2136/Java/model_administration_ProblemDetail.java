





import java.util.List;
import java.util.ArrayList;

public class model_administration_ProblemDetail  {

    private String instance;
    private String ecode;
    private int status;
    private String detail;



    public model_administration_ProblemDetail(
        String instance,        String ecode,        int status,        String detail    ) {
        this.instance = instance;
        this.ecode = ecode;
        this.status = status;
        this.detail = detail;
    }


    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }
    public String getEcode() {
        return ecode;
    }

    public void setEcode(String ecode) {
        this.ecode = ecode;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }


}