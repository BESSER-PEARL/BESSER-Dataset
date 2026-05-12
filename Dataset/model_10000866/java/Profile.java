





import java.util.List;
import java.util.ArrayList;

public class Profile  {






    private ListaEncadeada listaencadeada;


    public Profile(
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