





import java.util.List;
import java.util.ArrayList;

public class farrusco_Motor extends Actuate {

    private int Motor_Esquerdo;
    private int Motor_Direito;
    private String Nome;



    public farrusco_Motor(
        int Motor_Esquerdo,        int Motor_Direito,        String Nome    ) {
        super(
        );
        this.Motor_Esquerdo = Motor_Esquerdo;
        this.Motor_Direito = Motor_Direito;
        this.Nome = Nome;
    }


    public int getMotor_esquerdo() {
        return Motor_Esquerdo;
    }

    public void setMotor_esquerdo(int Motor_Esquerdo) {
        this.Motor_Esquerdo = Motor_Esquerdo;
    }
    public int getMotor_direito() {
        return Motor_Direito;
    }

    public void setMotor_direito(int Motor_Direito) {
        this.Motor_Direito = Motor_Direito;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}