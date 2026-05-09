





import java.util.List;
import java.util.ArrayList;

public class myDsl_ServiceFront extends AbstractFrontElement {

    private String name;
    private String method;





    private List<myDsl_AxiosRequest> mydsl_axiosrequests;


    public myDsl_ServiceFront(
        String name,        String method    ) {
        super(
        );
        this.name = name;
        this.method = method;
        this.mydsl_axiosrequests = new ArrayList<>();
    }

    public myDsl_ServiceFront(
        String name,        String method        ArrayList<myDsl_AxiosRequest> mydsl_axiosrequests    ) {
        this.name = name;
        this.method = method;
        this.mydsl_axiosrequests = mydsl_axiosrequests;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public List<myDsl_AxiosRequest> getMydsl_axiosrequests() {
        return mydsl_axiosrequests;
    }

    public void addMydsl_axiosrequest(Mydsl_axiosrequest mydsl_axiosrequest) {
        this.mydsl_axiosrequests.add(mydsl_axiosrequest);
    }

}