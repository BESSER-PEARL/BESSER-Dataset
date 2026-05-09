





import java.util.List;
import java.util.ArrayList;

public class domain_DataControl  {

    private String name;
    private String uid;





    private domain_ArtificialField domain_artificialfield;




    private domain_PREQueryTrigger domain_prequerytrigger;




    private domain_PREInsertTrigger domain_preinserttrigger;




    private domain_SourcesPointer domain_sourcespointer;




    private domain_SourcesPointer domain_sourcespointer;




    private domain_OptionSelection domain_optionselection;




    private domain_UpdateTrigger domain_updatetrigger;




    private domain_DeleteTrigger domain_deletetrigger;




    private domain_TypePointer domain_typepointer;




    private domain_Controls domain_controls;




    private domain_SearchTrigger domain_searchtrigger;




    private domain_OptionSelection domain_optionselection;




    private domain_POSTQueryTrigger domain_postquerytrigger;




    private domain_PREUpdateTrigger domain_preupdatetrigger;




    private domain_PREDeleteTrigger domain_predeletetrigger;




    private domain_InsertTrigger domain_inserttrigger;




    private List<domain_ArtificialField> domain_artificialfields;




    private domain_TypePointer domain_typepointer;




    private domain_POSTCreateTrigger domain_postcreatetrigger;




    private domain_ContextParameters domain_contextparameters;




    private domain_CreateTrigger domain_createtrigger;




    private domain_Controls domain_controls;


    public domain_DataControl(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
        this.domain_artificialfields = new ArrayList<>();
    }

    public domain_DataControl(
        String name,        String uid        ArrayList<domain_ArtificialField> domain_artificialfields    ) {
        this.name = name;
        this.uid = uid;
        this.domain_artificialfields = domain_artificialfields;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_ArtificialField getDomain_artificialfield() {
        return domain_artificialfield;
    }

    public void setDomain_artificialfield(domain_ArtificialField domain_artificialfield) {
        this.domain_artificialfield = domain_artificialfield;
    }
    public domain_PREQueryTrigger getDomain_prequerytrigger() {
        return domain_prequerytrigger;
    }

    public void setDomain_prequerytrigger(domain_PREQueryTrigger domain_prequerytrigger) {
        this.domain_prequerytrigger = domain_prequerytrigger;
    }
    public domain_PREInsertTrigger getDomain_preinserttrigger() {
        return domain_preinserttrigger;
    }

    public void setDomain_preinserttrigger(domain_PREInsertTrigger domain_preinserttrigger) {
        this.domain_preinserttrigger = domain_preinserttrigger;
    }
    public domain_SourcesPointer getDomain_sourcespointer() {
        return domain_sourcespointer;
    }

    public void setDomain_sourcespointer(domain_SourcesPointer domain_sourcespointer) {
        this.domain_sourcespointer = domain_sourcespointer;
    }
    public domain_SourcesPointer getDomain_sourcespointer() {
        return domain_sourcespointer;
    }

    public void setDomain_sourcespointer(domain_SourcesPointer domain_sourcespointer) {
        this.domain_sourcespointer = domain_sourcespointer;
    }
    public domain_OptionSelection getDomain_optionselection() {
        return domain_optionselection;
    }

    public void setDomain_optionselection(domain_OptionSelection domain_optionselection) {
        this.domain_optionselection = domain_optionselection;
    }
    public domain_UpdateTrigger getDomain_updatetrigger() {
        return domain_updatetrigger;
    }

    public void setDomain_updatetrigger(domain_UpdateTrigger domain_updatetrigger) {
        this.domain_updatetrigger = domain_updatetrigger;
    }
    public domain_DeleteTrigger getDomain_deletetrigger() {
        return domain_deletetrigger;
    }

    public void setDomain_deletetrigger(domain_DeleteTrigger domain_deletetrigger) {
        this.domain_deletetrigger = domain_deletetrigger;
    }
    public domain_TypePointer getDomain_typepointer() {
        return domain_typepointer;
    }

    public void setDomain_typepointer(domain_TypePointer domain_typepointer) {
        this.domain_typepointer = domain_typepointer;
    }
    public domain_Controls getDomain_controls() {
        return domain_controls;
    }

    public void setDomain_controls(domain_Controls domain_controls) {
        this.domain_controls = domain_controls;
    }
    public domain_SearchTrigger getDomain_searchtrigger() {
        return domain_searchtrigger;
    }

    public void setDomain_searchtrigger(domain_SearchTrigger domain_searchtrigger) {
        this.domain_searchtrigger = domain_searchtrigger;
    }
    public domain_OptionSelection getDomain_optionselection() {
        return domain_optionselection;
    }

    public void setDomain_optionselection(domain_OptionSelection domain_optionselection) {
        this.domain_optionselection = domain_optionselection;
    }
    public domain_POSTQueryTrigger getDomain_postquerytrigger() {
        return domain_postquerytrigger;
    }

    public void setDomain_postquerytrigger(domain_POSTQueryTrigger domain_postquerytrigger) {
        this.domain_postquerytrigger = domain_postquerytrigger;
    }
    public domain_PREUpdateTrigger getDomain_preupdatetrigger() {
        return domain_preupdatetrigger;
    }

    public void setDomain_preupdatetrigger(domain_PREUpdateTrigger domain_preupdatetrigger) {
        this.domain_preupdatetrigger = domain_preupdatetrigger;
    }
    public domain_PREDeleteTrigger getDomain_predeletetrigger() {
        return domain_predeletetrigger;
    }

    public void setDomain_predeletetrigger(domain_PREDeleteTrigger domain_predeletetrigger) {
        this.domain_predeletetrigger = domain_predeletetrigger;
    }
    public domain_InsertTrigger getDomain_inserttrigger() {
        return domain_inserttrigger;
    }

    public void setDomain_inserttrigger(domain_InsertTrigger domain_inserttrigger) {
        this.domain_inserttrigger = domain_inserttrigger;
    }
    public List<domain_ArtificialField> getDomain_artificialfields() {
        return domain_artificialfields;
    }

    public void addDomain_artificialfield(Domain_artificialfield domain_artificialfield) {
        this.domain_artificialfields.add(domain_artificialfield);
    }
    public domain_TypePointer getDomain_typepointer() {
        return domain_typepointer;
    }

    public void setDomain_typepointer(domain_TypePointer domain_typepointer) {
        this.domain_typepointer = domain_typepointer;
    }
    public domain_POSTCreateTrigger getDomain_postcreatetrigger() {
        return domain_postcreatetrigger;
    }

    public void setDomain_postcreatetrigger(domain_POSTCreateTrigger domain_postcreatetrigger) {
        this.domain_postcreatetrigger = domain_postcreatetrigger;
    }
    public domain_ContextParameters getDomain_contextparameters() {
        return domain_contextparameters;
    }

    public void setDomain_contextparameters(domain_ContextParameters domain_contextparameters) {
        this.domain_contextparameters = domain_contextparameters;
    }
    public domain_CreateTrigger getDomain_createtrigger() {
        return domain_createtrigger;
    }

    public void setDomain_createtrigger(domain_CreateTrigger domain_createtrigger) {
        this.domain_createtrigger = domain_createtrigger;
    }
    public domain_Controls getDomain_controls() {
        return domain_controls;
    }

    public void setDomain_controls(domain_Controls domain_controls) {
        this.domain_controls = domain_controls;
    }

}