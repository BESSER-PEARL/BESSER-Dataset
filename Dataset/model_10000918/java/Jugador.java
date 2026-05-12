





import java.util.List;
import java.util.ArrayList;

public class Jugador  {






    private List<Titulo> titulos;




    private TSalirCarcel tsalircarcel;




    private Monopoly monopoly;




    private Monopoly monopoly;


    public Jugador(
    ) {
        this.titulos = new ArrayList<>();
    }

    public Jugador(
        ArrayList<Titulo> titulos    ) {
        this.titulos = titulos;
    }


    public List<Titulo> getTitulos() {
        return titulos;
    }

    public void addTitulo(Titulo titulo) {
        this.titulos.add(titulo);
    }
    public TSalirCarcel getTsalircarcel() {
        return tsalircarcel;
    }

    public void setTsalircarcel(TSalirCarcel tsalircarcel) {
        this.tsalircarcel = tsalircarcel;
    }
    public Monopoly getMonopoly() {
        return monopoly;
    }

    public void setMonopoly(Monopoly monopoly) {
        this.monopoly = monopoly;
    }
    public Monopoly getMonopoly() {
        return monopoly;
    }

    public void setMonopoly(Monopoly monopoly) {
        this.monopoly = monopoly;
    }

}