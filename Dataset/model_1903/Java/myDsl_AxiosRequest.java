





import java.util.List;
import java.util.ArrayList;

public class myDsl_AxiosRequest extends AbstractFrontElement {

    private String name;
    private String axiosRestMethod;
    private String url;



    public myDsl_AxiosRequest(
        String name,        String axiosRestMethod,        String url    ) {
        super(
        );
        this.name = name;
        this.axiosRestMethod = axiosRestMethod;
        this.url = url;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAxiosrestmethod() {
        return axiosRestMethod;
    }

    public void setAxiosrestmethod(String axiosRestMethod) {
        this.axiosRestMethod = axiosRestMethod;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}