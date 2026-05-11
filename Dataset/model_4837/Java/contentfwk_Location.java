





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Location extends Element {






    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private contentfwk_Location contentfwk_location;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Actor> contentfwk_actors;


    public contentfwk_Location(
    ) {
        super(
        );
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_Location(
        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_actors = contentfwk_actors;
    }


    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }

}