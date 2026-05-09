





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Environment extends NamedElement {






    private List<mancoosimm_Alternative> mancoosimm_alternatives;




    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_Group mancoosimm_group;




    private mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog;




    private mancoosimm_Alternative mancoosimm_alternative;




    private mancoosimm_EmacsPackage mancoosimm_emacspackage;




    private mancoosimm_SGMLCatalog mancoosimm_sgmlcatalog;




    private mancoosimm_User mancoosimm_user;




    private mancoosimm_Configuration mancoosimm_configuration;




    private List<mancoosimm_Service> mancoosimm_services;




    private mancoosimm_EmacsPackage mancoosimm_emacspackage;




    private List<mancoosimm_Group> mancoosimm_groups;




    private mancoosimm_Service mancoosimm_service;




    private mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog;




    private List<mancoosimm_User> mancoosimm_users;




    private mancoosimm_SGMLCatalog mancoosimm_sgmlcatalog;


    public mancoosimm_Environment(
    ) {
        super(
        );
        this.mancoosimm_alternatives = new ArrayList<>();
        this.mancoosimm_services = new ArrayList<>();
        this.mancoosimm_groups = new ArrayList<>();
        this.mancoosimm_users = new ArrayList<>();
    }

    public mancoosimm_Environment(
        ArrayList<mancoosimm_Alternative> mancoosimm_alternatives,        ArrayList<mancoosimm_Service> mancoosimm_services,        ArrayList<mancoosimm_Group> mancoosimm_groups,        ArrayList<mancoosimm_User> mancoosimm_users    ) {
        this.mancoosimm_alternatives = mancoosimm_alternatives;
        this.mancoosimm_services = mancoosimm_services;
        this.mancoosimm_groups = mancoosimm_groups;
        this.mancoosimm_users = mancoosimm_users;
    }


    public List<mancoosimm_Alternative> getMancoosimm_alternatives() {
        return mancoosimm_alternatives;
    }

    public void addMancoosimm_alternative(Mancoosimm_alternative mancoosimm_alternative) {
        this.mancoosimm_alternatives.add(mancoosimm_alternative);
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public mancoosimm_Group getMancoosimm_group() {
        return mancoosimm_group;
    }

    public void setMancoosimm_group(mancoosimm_Group mancoosimm_group) {
        this.mancoosimm_group = mancoosimm_group;
    }
    public mancoosimm_SkeeperCatalog getMancoosimm_skeepercatalog() {
        return mancoosimm_skeepercatalog;
    }

    public void setMancoosimm_skeepercatalog(mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog) {
        this.mancoosimm_skeepercatalog = mancoosimm_skeepercatalog;
    }
    public mancoosimm_Alternative getMancoosimm_alternative() {
        return mancoosimm_alternative;
    }

    public void setMancoosimm_alternative(mancoosimm_Alternative mancoosimm_alternative) {
        this.mancoosimm_alternative = mancoosimm_alternative;
    }
    public mancoosimm_EmacsPackage getMancoosimm_emacspackage() {
        return mancoosimm_emacspackage;
    }

    public void setMancoosimm_emacspackage(mancoosimm_EmacsPackage mancoosimm_emacspackage) {
        this.mancoosimm_emacspackage = mancoosimm_emacspackage;
    }
    public mancoosimm_SGMLCatalog getMancoosimm_sgmlcatalog() {
        return mancoosimm_sgmlcatalog;
    }

    public void setMancoosimm_sgmlcatalog(mancoosimm_SGMLCatalog mancoosimm_sgmlcatalog) {
        this.mancoosimm_sgmlcatalog = mancoosimm_sgmlcatalog;
    }
    public mancoosimm_User getMancoosimm_user() {
        return mancoosimm_user;
    }

    public void setMancoosimm_user(mancoosimm_User mancoosimm_user) {
        this.mancoosimm_user = mancoosimm_user;
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public List<mancoosimm_Service> getMancoosimm_services() {
        return mancoosimm_services;
    }

    public void addMancoosimm_service(Mancoosimm_service mancoosimm_service) {
        this.mancoosimm_services.add(mancoosimm_service);
    }
    public mancoosimm_EmacsPackage getMancoosimm_emacspackage() {
        return mancoosimm_emacspackage;
    }

    public void setMancoosimm_emacspackage(mancoosimm_EmacsPackage mancoosimm_emacspackage) {
        this.mancoosimm_emacspackage = mancoosimm_emacspackage;
    }
    public List<mancoosimm_Group> getMancoosimm_groups() {
        return mancoosimm_groups;
    }

    public void addMancoosimm_group(Mancoosimm_group mancoosimm_group) {
        this.mancoosimm_groups.add(mancoosimm_group);
    }
    public mancoosimm_Service getMancoosimm_service() {
        return mancoosimm_service;
    }

    public void setMancoosimm_service(mancoosimm_Service mancoosimm_service) {
        this.mancoosimm_service = mancoosimm_service;
    }
    public mancoosimm_SkeeperCatalog getMancoosimm_skeepercatalog() {
        return mancoosimm_skeepercatalog;
    }

    public void setMancoosimm_skeepercatalog(mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog) {
        this.mancoosimm_skeepercatalog = mancoosimm_skeepercatalog;
    }
    public List<mancoosimm_User> getMancoosimm_users() {
        return mancoosimm_users;
    }

    public void addMancoosimm_user(Mancoosimm_user mancoosimm_user) {
        this.mancoosimm_users.add(mancoosimm_user);
    }
    public mancoosimm_SGMLCatalog getMancoosimm_sgmlcatalog() {
        return mancoosimm_sgmlcatalog;
    }

    public void setMancoosimm_sgmlcatalog(mancoosimm_SGMLCatalog mancoosimm_sgmlcatalog) {
        this.mancoosimm_sgmlcatalog = mancoosimm_sgmlcatalog;
    }

}