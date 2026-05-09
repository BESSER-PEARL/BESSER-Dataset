





import java.util.List;
import java.util.ArrayList;

public class ecore_hello  {






    private ecore_prueba ecore_prueba;




    private List<ecore_prueba> ecore_pruebas;


    public ecore_hello(
    ) {
        this.ecore_pruebas = new ArrayList<>();
    }

    public ecore_hello(
        ArrayList<ecore_prueba> ecore_pruebas    ) {
        this.ecore_pruebas = ecore_pruebas;
    }


    public ecore_prueba getEcore_prueba() {
        return ecore_prueba;
    }

    public void setEcore_prueba(ecore_prueba ecore_prueba) {
        this.ecore_prueba = ecore_prueba;
    }
    public List<ecore_prueba> getEcore_pruebas() {
        return ecore_pruebas;
    }

    public void addEcore_prueba(Ecore_prueba ecore_prueba) {
        this.ecore_pruebas.add(ecore_prueba);
    }

}