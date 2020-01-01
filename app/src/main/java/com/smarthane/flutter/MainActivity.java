package com.smarthane.flutter;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import com.smarthane.flutter.component.lib.FlutterEntryActivity;

/**
 * @author smarthane
 * @time 2020/1/1 10:45
 * @describe flutter host
 */
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.btnFlutterEntry).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, FlutterEntryActivity.class);
                startActivity(intent);
            }
        });
    }
}