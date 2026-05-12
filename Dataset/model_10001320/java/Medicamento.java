





import java.util.List;
import java.util.ArrayList;

public class Medicamento  {

    private String NomeComercial;
    private int Id;
    private String Fabricante;
    private String NomeGenerico;



    public Medicamento(
        String NomeComercial,        int Id,        String Fabricante,        String NomeGenerico    ) {
        this.NomeComercial = NomeComercial;
        this.Id = Id;
        this.Fabricante = Fabricante;
        this.NomeGenerico = NomeGenerico;
    }


    public String getNomecomercial() {
        return NomeComercial;
    }

    public void setNomecomercial(String NomeComercial) {
        this.NomeComercial = NomeComercial;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getFabricante() {
        return Fabricante;
    }

    public void setFabricante(String Fabricante) {
        this.Fabricante = Fabricante;
    }
    public String getNomegenerico() {
        return NomeGenerico;
    }

    public void setNomegenerico(String NomeGenerico) {
        this.NomeGenerico = NomeGenerico;
    }


}