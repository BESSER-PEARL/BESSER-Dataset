





import java.util.List;
import java.util.ArrayList;

public class Enfermeira  {

    private String cofen;
    private String setor;



    public Enfermeira(
        String cofen,        String setor    ) {
        this.cofen = cofen;
        this.setor = setor;
    }


    public String getCofen() {
        return cofen;
    }

    public void setCofen(String cofen) {
        this.cofen = cofen;
    }
    public String getSetor() {
        return setor;
    }

    public void setSetor(String setor) {
        this.setor = setor;
    }


}