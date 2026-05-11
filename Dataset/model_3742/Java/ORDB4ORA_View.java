





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_View extends DerivedTable {






    private List<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents;




    private List<ORDB4ORA_Table> ordb4ora_tables;


    public ORDB4ORA_View(
    ) {
        super(
        );
        this.ordb4ora_structuralcomponents = new ArrayList<>();
        this.ordb4ora_tables = new ArrayList<>();
    }

    public ORDB4ORA_View(
        ArrayList<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents,        ArrayList<ORDB4ORA_Table> ordb4ora_tables    ) {
        this.ordb4ora_structuralcomponents = ordb4ora_structuralcomponents;
        this.ordb4ora_tables = ordb4ora_tables;
    }


    public List<ORDB4ORA_StructuralComponent> getOrdb4ora_structuralcomponents() {
        return ordb4ora_structuralcomponents;
    }

    public void addOrdb4ora_structuralcomponent(Ordb4ora_structuralcomponent ordb4ora_structuralcomponent) {
        this.ordb4ora_structuralcomponents.add(ordb4ora_structuralcomponent);
    }
    public List<ORDB4ORA_Table> getOrdb4ora_tables() {
        return ordb4ora_tables;
    }

    public void addOrdb4ora_table(Ordb4ora_table ordb4ora_table) {
        this.ordb4ora_tables.add(ordb4ora_table);
    }

}