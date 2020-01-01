package com.smarthane.flutter.component.lib;

import android.support.annotation.NonNull;
import android.widget.Toast;

import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;
import io.flutter.plugins.GeneratedPluginRegistrant;

/**
 * @author smarthane
 * @time 2020/1/1 10:45
 * @describe flutter lib ,flutter组件入口
 */
public class FlutterEntryActivity extends FlutterActivity {

    @Override
    public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
        GeneratedPluginRegistrant.registerWith(flutterEngine);
        new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), "test_channel").setMethodCallHandler(new MethodChannel.MethodCallHandler() {
            @Override
            public void onMethodCall(@NonNull MethodCall call, @NonNull MethodChannel.Result result) {
                switch (call.method) {
                    case "toaseEvent":
                        showToast();
                        result.success(true);
                        break;
                    default:
                        result.notImplemented();
                }
            }
        });
    }

    private void showToast() {
        Toast.makeText(this, "show toast success", Toast.LENGTH_LONG).show();
    }
}
