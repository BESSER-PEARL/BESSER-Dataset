





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Service extends Standard {






    private List<contentfwk_Contract> contentfwk_contracts;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_Event contentfwk_event;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents;




    private List<contentfwk_Measure> contentfwk_measures;




    private List<contentfwk_Event> contentfwk_events;




    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_Measure contentfwk_measure;




    private List<contentfwk_DataEntity> contentfwk_dataentitys;




    private List<contentfwk_ServiceQuality> contentfwk_servicequalitys;




    private contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent;




    private contentfwk_Contract contentfwk_contract;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Service> contentfwk_services;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_DataEntity> contentfwk_dataentitys;




    private contentfwk_ServiceQuality contentfwk_servicequality;




    private List<contentfwk_Service> contentfwk_services;


    public contentfwk_Service(
    ) {
        super(
        );
        this.contentfwk_contracts = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_logicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_measures = new ArrayList<>();
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_dataentitys = new ArrayList<>();
        this.contentfwk_servicequalitys = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_dataentitys = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
    }

    public contentfwk_Service(
        ArrayList<contentfwk_Contract> contentfwk_contracts,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents,        ArrayList<contentfwk_Measure> contentfwk_measures,        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_DataEntity> contentfwk_dataentitys,        ArrayList<contentfwk_ServiceQuality> contentfwk_servicequalitys,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_DataEntity> contentfwk_dataentitys,        ArrayList<contentfwk_Service> contentfwk_services    ) {
        this.contentfwk_contracts = contentfwk_contracts;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_logicaltechnologycomponents = contentfwk_logicaltechnologycomponents;
        this.contentfwk_measures = contentfwk_measures;
        this.contentfwk_events = contentfwk_events;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_dataentitys = contentfwk_dataentitys;
        this.contentfwk_servicequalitys = contentfwk_servicequalitys;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_dataentitys = contentfwk_dataentitys;
        this.contentfwk_services = contentfwk_services;
    }


    public List<contentfwk_Contract> getContentfwk_contracts() {
        return contentfwk_contracts;
    }

    public void addContentfwk_contract(Contentfwk_contract contentfwk_contract) {
        this.contentfwk_contracts.add(contentfwk_contract);
    }
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_Event getContentfwk_event() {
        return contentfwk_event;
    }

    public void setContentfwk_event(contentfwk_Event contentfwk_event) {
        this.contentfwk_event = contentfwk_event;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public List<contentfwk_LogicalTechnologyComponent> getContentfwk_logicaltechnologycomponents() {
        return contentfwk_logicaltechnologycomponents;
    }

    public void addContentfwk_logicaltechnologycomponent(Contentfwk_logicaltechnologycomponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponents.add(contentfwk_logicaltechnologycomponent);
    }
    public List<contentfwk_Measure> getContentfwk_measures() {
        return contentfwk_measures;
    }

    public void addContentfwk_measure(Contentfwk_measure contentfwk_measure) {
        this.contentfwk_measures.add(contentfwk_measure);
    }
    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_Measure getContentfwk_measure() {
        return contentfwk_measure;
    }

    public void setContentfwk_measure(contentfwk_Measure contentfwk_measure) {
        this.contentfwk_measure = contentfwk_measure;
    }
    public List<contentfwk_DataEntity> getContentfwk_dataentitys() {
        return contentfwk_dataentitys;
    }

    public void addContentfwk_dataentity(Contentfwk_dataentity contentfwk_dataentity) {
        this.contentfwk_dataentitys.add(contentfwk_dataentity);
    }
    public List<contentfwk_ServiceQuality> getContentfwk_servicequalitys() {
        return contentfwk_servicequalitys;
    }

    public void addContentfwk_servicequality(Contentfwk_servicequality contentfwk_servicequality) {
        this.contentfwk_servicequalitys.add(contentfwk_servicequality);
    }
    public contentfwk_LogicalTechnologyComponent getContentfwk_logicaltechnologycomponent() {
        return contentfwk_logicaltechnologycomponent;
    }

    public void setContentfwk_logicaltechnologycomponent(contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponent = contentfwk_logicaltechnologycomponent;
    }
    public contentfwk_Contract getContentfwk_contract() {
        return contentfwk_contract;
    }

    public void setContentfwk_contract(contentfwk_Contract contentfwk_contract) {
        this.contentfwk_contract = contentfwk_contract;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_DataEntity> getContentfwk_dataentitys() {
        return contentfwk_dataentitys;
    }

    public void addContentfwk_dataentity(Contentfwk_dataentity contentfwk_dataentity) {
        this.contentfwk_dataentitys.add(contentfwk_dataentity);
    }
    public contentfwk_ServiceQuality getContentfwk_servicequality() {
        return contentfwk_servicequality;
    }

    public void setContentfwk_servicequality(contentfwk_ServiceQuality contentfwk_servicequality) {
        this.contentfwk_servicequality = contentfwk_servicequality;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }

}