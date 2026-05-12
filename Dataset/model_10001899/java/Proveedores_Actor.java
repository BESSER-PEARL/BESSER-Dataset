





import java.util.List;
import java.util.ArrayList;

public class Proveedores_Actor  {






    private Recibir_productos_o_pedidos_external recibir_productos_o_pedidos_external;




    private Registrar_proveedores_external registrar_proveedores_external;


    public Proveedores_Actor(
    ) {
    }



    public Recibir_productos_o_pedidos_external getRecibir_productos_o_pedidos_external() {
        return recibir_productos_o_pedidos_external;
    }

    public void setRecibir_productos_o_pedidos_external(Recibir_productos_o_pedidos_external recibir_productos_o_pedidos_external) {
        this.recibir_productos_o_pedidos_external = recibir_productos_o_pedidos_external;
    }
    public Registrar_proveedores_external getRegistrar_proveedores_external() {
        return registrar_proveedores_external;
    }

    public void setRegistrar_proveedores_external(Registrar_proveedores_external registrar_proveedores_external) {
        this.registrar_proveedores_external = registrar_proveedores_external;
    }

}