





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Location extends Element {






    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_Location contentfwk_location;


    public contentfwk_Location(
    ) {
        super(
        );
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_Location(
        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_actors = contentfwk_actors;
    }


    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }

}