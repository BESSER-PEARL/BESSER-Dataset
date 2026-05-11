





import java.util.List;
import java.util.ArrayList;

public class go_Assignment  {

    private String qtd;
    private String id;





    private go_IGUAL go_igual;




    private go_EXPRESSAO go_expressao;




    private go_EXPRESSAOLINHA go_expressaolinha;




    private go_PONTOSIGUAL go_pontosigual;


    public go_Assignment(
        String qtd,        String id    ) {
        this.qtd = qtd;
        this.id = id;
    }


    public String getQtd() {
        return qtd;
    }

    public void setQtd(String qtd) {
        this.qtd = qtd;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public go_IGUAL getGo_igual() {
        return go_igual;
    }

    public void setGo_igual(go_IGUAL go_igual) {
        this.go_igual = go_igual;
    }
    public go_EXPRESSAO getGo_expressao() {
        return go_expressao;
    }

    public void setGo_expressao(go_EXPRESSAO go_expressao) {
        this.go_expressao = go_expressao;
    }
    public go_EXPRESSAOLINHA getGo_expressaolinha() {
        return go_expressaolinha;
    }

    public void setGo_expressaolinha(go_EXPRESSAOLINHA go_expressaolinha) {
        this.go_expressaolinha = go_expressaolinha;
    }
    public go_PONTOSIGUAL getGo_pontosigual() {
        return go_pontosigual;
    }

    public void setGo_pontosigual(go_PONTOSIGUAL go_pontosigual) {
        this.go_pontosigual = go_pontosigual;
    }

}