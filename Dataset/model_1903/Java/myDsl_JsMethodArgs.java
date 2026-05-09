





import java.util.List;
import java.util.ArrayList;

public class myDsl_JsMethodArgs  {

    private String name;





    private myDsl_JsMethod mydsl_jsmethod;




    private myDsl_AxiosRequest mydsl_axiosrequest;


    public myDsl_JsMethodArgs(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_JsMethod getMydsl_jsmethod() {
        return mydsl_jsmethod;
    }

    public void setMydsl_jsmethod(myDsl_JsMethod mydsl_jsmethod) {
        this.mydsl_jsmethod = mydsl_jsmethod;
    }
    public myDsl_AxiosRequest getMydsl_axiosrequest() {
        return mydsl_axiosrequest;
    }

    public void setMydsl_axiosrequest(myDsl_AxiosRequest mydsl_axiosrequest) {
        this.mydsl_axiosrequest = mydsl_axiosrequest;
    }

}