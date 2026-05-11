





import java.util.List;
import java.util.ArrayList;

public class Selects_From  {






    private Selects_Select selects_select;




    private List<Selects_Tabla> selects_tablas;


    public Selects_From(
    ) {
        this.selects_tablas = new ArrayList<>();
    }

    public Selects_From(
        ArrayList<Selects_Tabla> selects_tablas    ) {
        this.selects_tablas = selects_tablas;
    }


    public Selects_Select getSelects_select() {
        return selects_select;
    }

    public void setSelects_select(Selects_Select selects_select) {
        this.selects_select = selects_select;
    }
    public List<Selects_Tabla> getSelects_tablas() {
        return selects_tablas;
    }

    public void addSelects_tabla(Selects_tabla selects_tabla) {
        this.selects_tablas.add(selects_tabla);
    }

}