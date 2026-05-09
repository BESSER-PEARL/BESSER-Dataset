





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ReactServiceRequestProps  {

    private String reqPropDescription;
    private String reqPropName;





    private softGalleryLanguage_ReactServiceContRequest softgallerylanguage_reactservicecontrequest;


    public softGalleryLanguage_ReactServiceRequestProps(
        String reqPropDescription,        String reqPropName    ) {
        this.reqPropDescription = reqPropDescription;
        this.reqPropName = reqPropName;
    }


    public String getReqpropdescription() {
        return reqPropDescription;
    }

    public void setReqpropdescription(String reqPropDescription) {
        this.reqPropDescription = reqPropDescription;
    }
    public String getReqpropname() {
        return reqPropName;
    }

    public void setReqpropname(String reqPropName) {
        this.reqPropName = reqPropName;
    }

    public softGalleryLanguage_ReactServiceContRequest getSoftgallerylanguage_reactservicecontrequest() {
        return softgallerylanguage_reactservicecontrequest;
    }

    public void setSoftgallerylanguage_reactservicecontrequest(softGalleryLanguage_ReactServiceContRequest softgallerylanguage_reactservicecontrequest) {
        this.softgallerylanguage_reactservicecontrequest = softgallerylanguage_reactservicecontrequest;
    }

}