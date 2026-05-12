





import java.util.List;
import java.util.ArrayList;

public class Vendedor_Actor1  {






    private Vender_producto_UseCase vender_producto_usecase;




    private Registrar_venta_UseCase registrar_venta_usecase;


    public Vendedor_Actor1(
    ) {
    }



    public Vender_producto_UseCase getVender_producto_usecase() {
        return vender_producto_usecase;
    }

    public void setVender_producto_usecase(Vender_producto_UseCase vender_producto_usecase) {
        this.vender_producto_usecase = vender_producto_usecase;
    }
    public Registrar_venta_UseCase getRegistrar_venta_usecase() {
        return registrar_venta_usecase;
    }

    public void setRegistrar_venta_usecase(Registrar_venta_UseCase registrar_venta_usecase) {
        this.registrar_venta_usecase = registrar_venta_usecase;
    }

}