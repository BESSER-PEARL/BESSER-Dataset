





import java.util.List;
import java.util.ArrayList;

public class Post  {






    private ListaEncadeada listaencadeada;


    public Post(
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