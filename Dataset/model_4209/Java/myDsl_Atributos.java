





import java.util.List;
import java.util.ArrayList;

public class myDsl_Atributos  {






    private myDsl_Entidade mydsl_entidade;




    private myDsl_Atributo mydsl_atributo;




    private List<myDsl_Atributo> mydsl_atributos;


    public myDsl_Atributos(
    ) {
        this.mydsl_atributos = new ArrayList<>();
    }

    public myDsl_Atributos(
        ArrayList<myDsl_Atributo> mydsl_atributos    ) {
        this.mydsl_atributos = mydsl_atributos;
    }


    public myDsl_Entidade getMydsl_entidade() {
        return mydsl_entidade;
    }

    public void setMydsl_entidade(myDsl_Entidade mydsl_entidade) {
        this.mydsl_entidade = mydsl_entidade;
    }
    public myDsl_Atributo getMydsl_atributo() {
        return mydsl_atributo;
    }

    public void setMydsl_atributo(myDsl_Atributo mydsl_atributo) {
        this.mydsl_atributo = mydsl_atributo;
    }
    public List<myDsl_Atributo> getMydsl_atributos() {
        return mydsl_atributos;
    }

    public void addMydsl_atributo(Mydsl_atributo mydsl_atributo) {
        this.mydsl_atributos.add(mydsl_atributo);
    }

}