





import java.util.List;
import java.util.ArrayList;

public class sadl_DisjointClasses extends Statement {






    private sadl_ExistingResourceList sadl_existingresourcelist;




    private sadl_ResourceByName sadl_resourcebyname;




    private sadl_ResourceIdentifier sadl_resourceidentifier;


    public sadl_DisjointClasses(
    ) {
        super(
        );
    }



    public sadl_ExistingResourceList getSadl_existingresourcelist() {
        return sadl_existingresourcelist;
    }

    public void setSadl_existingresourcelist(sadl_ExistingResourceList sadl_existingresourcelist) {
        this.sadl_existingresourcelist = sadl_existingresourcelist;
    }
    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }

}