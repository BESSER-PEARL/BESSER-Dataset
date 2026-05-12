





import java.util.List;
import java.util.ArrayList;

public class Message  {






    private ListaEncadeada listaencadeada;


    public Message(
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