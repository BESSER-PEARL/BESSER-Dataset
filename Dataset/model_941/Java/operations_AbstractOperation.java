





import java.util.List;
import java.util.ArrayList;

public class operations_AbstractOperation  {






    private esmodel_events_UndoEvent esmodel_events_undoevent;




    private esmodel_versioning_ChangePackage esmodel_versioning_changepackage;


    public operations_AbstractOperation(
    ) {
    }



    public esmodel_events_UndoEvent getEsmodel_events_undoevent() {
        return esmodel_events_undoevent;
    }

    public void setEsmodel_events_undoevent(esmodel_events_UndoEvent esmodel_events_undoevent) {
        this.esmodel_events_undoevent = esmodel_events_undoevent;
    }
    public esmodel_versioning_ChangePackage getEsmodel_versioning_changepackage() {
        return esmodel_versioning_changepackage;
    }

    public void setEsmodel_versioning_changepackage(esmodel_versioning_ChangePackage esmodel_versioning_changepackage) {
        this.esmodel_versioning_changepackage = esmodel_versioning_changepackage;
    }

}