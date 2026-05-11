





import java.util.List;
import java.util.ArrayList;

public class myDsl_AtributoTipo  {

    private String tipoObjeto;
    private String tipoPrimitivo;
    private String tipoColecao;





    private myDsl_Atributo mydsl_atributo;


    public myDsl_AtributoTipo(
        String tipoObjeto,        String tipoPrimitivo,        String tipoColecao    ) {
        this.tipoObjeto = tipoObjeto;
        this.tipoPrimitivo = tipoPrimitivo;
        this.tipoColecao = tipoColecao;
    }


    public String getTipoobjeto() {
        return tipoObjeto;
    }

    public void setTipoobjeto(String tipoObjeto) {
        this.tipoObjeto = tipoObjeto;
    }
    public String getTipoprimitivo() {
        return tipoPrimitivo;
    }

    public void setTipoprimitivo(String tipoPrimitivo) {
        this.tipoPrimitivo = tipoPrimitivo;
    }
    public String getTipocolecao() {
        return tipoColecao;
    }

    public void setTipocolecao(String tipoColecao) {
        this.tipoColecao = tipoColecao;
    }

    public myDsl_Atributo getMydsl_atributo() {
        return mydsl_atributo;
    }

    public void setMydsl_atributo(myDsl_Atributo mydsl_atributo) {
        this.mydsl_atributo = mydsl_atributo;
    }

}