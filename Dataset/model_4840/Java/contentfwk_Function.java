





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Function extends Standard, Element {






    private contentfwk_Function contentfwk_function;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_Role> contentfwk_roles;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Role contentfwk_role;




    private List<contentfwk_Actor> contentfwk_actors;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Function(
    ) {
        super(
        );
        this.contentfwk_roles = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_Function(
        ArrayList<contentfwk_Role> contentfwk_roles,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.contentfwk_roles = contentfwk_roles;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_actors = contentfwk_actors;
    }


    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_Role> getContentfwk_roles() {
        return contentfwk_roles;
    }

    public void addContentfwk_role(Contentfwk_role contentfwk_role) {
        this.contentfwk_roles.add(contentfwk_role);
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Role getContentfwk_role() {
        return contentfwk_role;
    }

    public void setContentfwk_role(contentfwk_Role contentfwk_role) {
        this.contentfwk_role = contentfwk_role;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}