





import java.util.List;
import java.util.ArrayList;

public class transacao_transferencia  {

    private None contaAlvo;
    private None contaOrigem;



    public transacao_transferencia(
        None contaAlvo,        None contaOrigem    ) {
        this.contaAlvo = contaAlvo;
        this.contaOrigem = contaOrigem;
    }


    public None getContaalvo() {
        return contaAlvo;
    }

    public void setContaalvo(None contaAlvo) {
        this.contaAlvo = contaAlvo;
    }
    public None getContaorigem() {
        return contaOrigem;
    }

    public void setContaorigem(None contaOrigem) {
        this.contaOrigem = contaOrigem;
    }


}