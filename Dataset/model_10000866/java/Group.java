





import java.util.List;
import java.util.ArrayList;

public class Group  {






    private ListaEncadeada listaencadeada;


    public Group(
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