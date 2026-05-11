





import java.util.List;
import java.util.ArrayList;

public class caracteristica_EntidadeDeContexto extends Elemento {






    private caracteristica_RaizDeContexto caracteristica_raizdecontexto;




    private caracteristica_InformacaoDeContexto caracteristica_informacaodecontexto;




    private List<caracteristica_InformacaoDeContexto> caracteristica_informacaodecontextos;




    private caracteristica_RaizDeContexto caracteristica_raizdecontexto;


    public caracteristica_EntidadeDeContexto(
    ) {
        super(
        );
        this.caracteristica_informacaodecontextos = new ArrayList<>();
    }

    public caracteristica_EntidadeDeContexto(
        ArrayList<caracteristica_InformacaoDeContexto> caracteristica_informacaodecontextos    ) {
        this.caracteristica_informacaodecontextos = caracteristica_informacaodecontextos;
    }


    public caracteristica_RaizDeContexto getCaracteristica_raizdecontexto() {
        return caracteristica_raizdecontexto;
    }

    public void setCaracteristica_raizdecontexto(caracteristica_RaizDeContexto caracteristica_raizdecontexto) {
        this.caracteristica_raizdecontexto = caracteristica_raizdecontexto;
    }
    public caracteristica_InformacaoDeContexto getCaracteristica_informacaodecontexto() {
        return caracteristica_informacaodecontexto;
    }

    public void setCaracteristica_informacaodecontexto(caracteristica_InformacaoDeContexto caracteristica_informacaodecontexto) {
        this.caracteristica_informacaodecontexto = caracteristica_informacaodecontexto;
    }
    public List<caracteristica_InformacaoDeContexto> getCaracteristica_informacaodecontextos() {
        return caracteristica_informacaodecontextos;
    }

    public void addCaracteristica_informacaodecontexto(Caracteristica_informacaodecontexto caracteristica_informacaodecontexto) {
        this.caracteristica_informacaodecontextos.add(caracteristica_informacaodecontexto);
    }
    public caracteristica_RaizDeContexto getCaracteristica_raizdecontexto() {
        return caracteristica_raizdecontexto;
    }

    public void setCaracteristica_raizdecontexto(caracteristica_RaizDeContexto caracteristica_raizdecontexto) {
        this.caracteristica_raizdecontexto = caracteristica_raizdecontexto;
    }

}