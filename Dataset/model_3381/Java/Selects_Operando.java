





import java.util.List;
import java.util.ArrayList;

public class Selects_Operando  {

    private String tabla;
    private String columna;





    private Selects_Join selects_join;




    private Selects_Join selects_join;


    public Selects_Operando(
        String tabla,        String columna    ) {
        this.tabla = tabla;
        this.columna = columna;
    }


    public String getTabla() {
        return tabla;
    }

    public void setTabla(String tabla) {
        this.tabla = tabla;
    }
    public String getColumna() {
        return columna;
    }

    public void setColumna(String columna) {
        this.columna = columna;
    }

    public Selects_Join getSelects_join() {
        return selects_join;
    }

    public void setSelects_join(Selects_Join selects_join) {
        this.selects_join = selects_join;
    }
    public Selects_Join getSelects_join() {
        return selects_join;
    }

    public void setSelects_join(Selects_Join selects_join) {
        this.selects_join = selects_join;
    }

}