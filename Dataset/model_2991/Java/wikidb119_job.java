





import java.util.List;
import java.util.ArrayList;

public class wikidb119_job  {

    private String job_id;
    private String job_cmd;
    private String job_params;
    private String job_namespace;
    private String job_title;
    private String job_timestamp;



    public wikidb119_job(
        String job_id,        String job_cmd,        String job_params,        String job_namespace,        String job_title,        String job_timestamp    ) {
        this.job_id = job_id;
        this.job_cmd = job_cmd;
        this.job_params = job_params;
        this.job_namespace = job_namespace;
        this.job_title = job_title;
        this.job_timestamp = job_timestamp;
    }


    public String getJob_id() {
        return job_id;
    }

    public void setJob_id(String job_id) {
        this.job_id = job_id;
    }
    public String getJob_cmd() {
        return job_cmd;
    }

    public void setJob_cmd(String job_cmd) {
        this.job_cmd = job_cmd;
    }
    public String getJob_params() {
        return job_params;
    }

    public void setJob_params(String job_params) {
        this.job_params = job_params;
    }
    public String getJob_namespace() {
        return job_namespace;
    }

    public void setJob_namespace(String job_namespace) {
        this.job_namespace = job_namespace;
    }
    public String getJob_title() {
        return job_title;
    }

    public void setJob_title(String job_title) {
        this.job_title = job_title;
    }
    public String getJob_timestamp() {
        return job_timestamp;
    }

    public void setJob_timestamp(String job_timestamp) {
        this.job_timestamp = job_timestamp;
    }


}