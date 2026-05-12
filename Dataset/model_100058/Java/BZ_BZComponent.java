





import java.util.List;
import java.util.ArrayList;

public class BZ_BZComponent  {

    private String componentURL;
    private String componentDescription;
    private String defaultAssignee;
    private String componentId;





    private BZ_BZProduct bz_bzproduct;




    private BZ_BZRepo bz_bzrepo;




    private BZ_BZRepo bz_bzrepo;




    private BZ_BZProduct bz_bzproduct;


    public BZ_BZComponent(
        String componentURL,        String componentDescription,        String defaultAssignee,        String componentId    ) {
        this.componentURL = componentURL;
        this.componentDescription = componentDescription;
        this.defaultAssignee = defaultAssignee;
        this.componentId = componentId;
    }


    public String getComponenturl() {
        return componentURL;
    }

    public void setComponenturl(String componentURL) {
        this.componentURL = componentURL;
    }
    public String getComponentdescription() {
        return componentDescription;
    }

    public void setComponentdescription(String componentDescription) {
        this.componentDescription = componentDescription;
    }
    public String getDefaultassignee() {
        return defaultAssignee;
    }

    public void setDefaultassignee(String defaultAssignee) {
        this.defaultAssignee = defaultAssignee;
    }
    public String getComponentid() {
        return componentId;
    }

    public void setComponentid(String componentId) {
        this.componentId = componentId;
    }

    public BZ_BZProduct getBz_bzproduct() {
        return bz_bzproduct;
    }

    public void setBz_bzproduct(BZ_BZProduct bz_bzproduct) {
        this.bz_bzproduct = bz_bzproduct;
    }
    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }
    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }
    public BZ_BZProduct getBz_bzproduct() {
        return bz_bzproduct;
    }

    public void setBz_bzproduct(BZ_BZProduct bz_bzproduct) {
        this.bz_bzproduct = bz_bzproduct;
    }

}