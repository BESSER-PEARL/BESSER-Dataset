





import java.util.List;
import java.util.ArrayList;

public class Login  {






    private ListaEncadeada listaencadeada;


    public Login(
    ) {
        this.listaencadeadas = new ArrayList<>();
    }



    public ListaEncadeada getListaencadeadas() {
        return listaencadeadas;
    }

    public void addListaencadeada(Listaencadeada listaencadeada) {
        this.listaencadeadas.add(listaencadeada);
    }

}